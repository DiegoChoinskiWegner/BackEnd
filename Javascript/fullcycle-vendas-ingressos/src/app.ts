import express from 'express';
import * as mysql from 'mysql2/promise';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';



function createConnection(){
    return mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'root', 
        database: 'tickets'
    })
}

const app = express();

app.use(express.json())

const unprotectedRoutes = [
    {method: 'GET', path: '/events'},
    {method: 'POST', path: '/auth/login'},
    {method: 'POST', path: '/costumers/register'},
    {method: 'POST', path: '/partners/register'}
]


app.use(async (req, res, next) => {

    const isUnprotectedRoute = unprotectedRoutes.some(route => route.method == req.method && req.path.startsWith(route.path))

    if(isUnprotectedRoute){
        next();
        return;
    }


    const token = req.headers['authorization']?.split(' ')[1];
    if(!token){
        res.status(401).json({message: 'Unauthorized'});
        return;
    }
  
    try{
        const payload = jwt.verify(token, "123456") as {id: number, email: string};
        const connection = await createConnection();
        const [rows] = await connection.execute<mysql.RowDataPacket[]>('SELECT * FROM users WHERE id = ?', [payload.id]);
        const user = rows.lenght ? rows[0]: null;
        if(!user){
            res.status(401).json({message: 'Unauthorized'});
            return;
        }
        req.user = user;
        next();
    }catch(error){
        res.status(401).json({message: 'Unauthorized'});
        return;
    }
    
})


app.get('/', (req, res) =>{
    res.json({message:"Hello, World!"})
})

app.post('/auth/login', async (req, res) =>{
    const { email, password } = req.body;

    const connection = await createConnection();

    try{
        const [rows] = await connection.execute<mysql.RowDataPacket[]>('SELECT * FROM users WHERE email = ?', [email]);
        const user = rows.lenght ? rows[0]: null
        if(user && bcrypt.compareSync(password, user.password)){
            const token = jwt.sign({id: user.id, email: user.email}, "123456", {expiresIn: '1h'})
            res.json({token})
            res.status(200).json({message: 'Logged in successfully'})
        }else{
            res.status(401).json({message: 'Invalid credentials'});
        }
    }finally {
        await connection.end();
    }
})



app.post('/partners', async (req, res) => {
    const { name, email, password, company_name } = req.body;

    const connection = await createConnection();
    
    try{
        const cratedAt = new Date()
        const hashedPassword = bcrypt.hashSync(password, 10);

        const [userResult] = await connection.execute<mysql.ResultSetHeader>('INSERTO INTO users (name, email, password, created_at)', [
            name,
            email,
            hashedPassword,
            cratedAt
        ])

        const userId = userResult.insertId;

        const [partnerResult] = await connection.execute<mysql.ResultSetHeader>('INSERTO INTO partners (user_id, company_name, created_at)', [
            userId,
            company_name,
            cratedAt
        ])

        res.status(201).json({id: partnerResult.insertId, userId, company_name, cratedAt, message: 'Partner created successfully' });
    }finally {
        await connection.end();
    }
})

app.post('/customers', (req, res) =>{
    const { name, email, password, adress, telefone } = req.body;
})

app.post('/partners/events', async (req, res) =>{
    const { name, description, date, location } = req.body;
    const userId = req.user!.id

    const connection = createConnection();
    const [rows] = await connection.execute<mysql.RowDataPacket[]>(
        'SELECT * FROM partners WHERE user_id = ?', [userId]
    );

    const partner = rows.lenght ? rows[0]: null;

    if(!partner){
        res.status(403).json({message: 'Unauthorized'});
        return;
    }

    const [partnerResult] = await connection.execute<mysql.ResultSetHeader>(
        "INSERT INTO events (name, description, date, location, partner_id, cratedAt) VALUES (?, ?, ?, ?, ?, ?)",
        [name, description,new Date(date), location, partner.id, new Date()]
    );

    res.status(201).json({id: partnerResult.insertId, name, description, date, location, partner_id: partner.id});
    await connection.end();
})

app.get('/partners/events', (req, res) =>{

})

app.get('/partners/events/:eventId', (req, res) =>{
    const { eventId } = req.params;
    console.log(eventId);
    res.send();
})

app.get('/events', (req, res) =>{

})

app.get('/events/:eventId', (req, res) =>{
    const { eventId } = req.params;
    console.log(eventId);
    res.send();
})

app.post('/tickets', (req, res) =>{
    const { id, value, description, date, location } = req.body;
})

app.listen(3000, () => {
    console.log("Running in http://localhost:3000")
})