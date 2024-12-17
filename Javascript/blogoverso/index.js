// Função para verificar se o usuário já está cadastrado
function checkUser(username) {
    let users = JSON.parse(localStorage.getItem('users')) || [];
    return users.find(user => user.username === username);
}

// Função para registrar um novo usuário
function register() {
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;
  
    // Criação do novo usuário usando Firebase Authentication
    auth.createUserWithEmailAndPassword(username + "@example.com", password)
      .then(userCredential => {
        const user = userCredential.user;
  
        // Criar documento no Firestore para armazenar dados do usuário
        db.collection("users").doc(user.uid).set({
          username: username,
          posts: []
        })
        .then(() => {
          alert('Usuário cadastrado com sucesso!');
          window.location.href = 'index.html';
        })
        .catch(error => {
          console.error("Erro ao registrar usuário: ", error);
          alert("Erro ao registrar usuário: " + error.message);
        });
      })
      .catch(error => {
        console.error("Erro ao criar usuário: ", error);
        alert("Erro ao criar usuário: " + error.message);
      });
  }

// Função para realizar login
function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    // Login com Firebase Authentication
    auth.signInWithEmailAndPassword(username + "@example.com", password)
      .then(userCredential => {
        const user = userCredential.user;
  
        // Salvar dados do usuário logado no localStorage (opcional)
        localStorage.setItem('loggedInUser', JSON.stringify(user));
  
        window.location.href = 'dashboard.html';
      })
      .catch(error => {
        console.error("Erro ao fazer login: ", error);
        alert("Erro ao fazer login: " + error.message);
      });
  }

// Função para carregar o painel do usuário
function loadDashboard() {
    const user = JSON.parse(localStorage.getItem('loggedInUser'));
  
    if (!user) {
      window.location.href = 'index.html';
      return;
    }
  
    document.getElementById('logged-user').textContent = user.email.split('@')[0]; // Exibe o nome do usuário (sem o @example.com)
  
    // Carregar postagens do Firestore
    db.collection("users").doc(user.uid).get()
      .then(doc => {
        if (doc.exists) {
          const posts = doc.data().posts;
          displayPosts(posts);
        }
      })
      .catch(error => {
        console.error("Erro ao carregar postagens: ", error);
      });
  }

// Função para exibir as postagens do usuário
function displayPosts(posts) {
    const postsList = document.getElementById('posts-list');
    postsList.innerHTML = '';
    posts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.innerHTML = `<h3>${post.title}</h3><p>${post.content}</p>`;
        postsList.appendChild(postElement);
    });
}

// Função para criar uma nova postagem
function createPost() {
  const title = prompt("Título da postagem:");
  const content = prompt("Conteúdo da postagem:");

  const user = JSON.parse(localStorage.getItem('loggedInUser'));

  if (user) {
    // Adicionar a postagem ao Firestore
    db.collection("users").doc(user.uid)
      .update({
        posts: firebase.firestore.FieldValue.arrayUnion({ title, content })
      })
      .then(() => {
        alert('Postagem criada com sucesso!');
        loadDashboard(); // Recarregar o painel após adicionar a postagem
      })
      .catch(error => {
        console.error("Erro ao criar postagem: ", error);
      });
  }
}

// Função para fazer logout
function logout() {
    auth.signOut().then(() => {
      localStorage.removeItem('loggedInUser');
      window.location.href = 'index.html';
    }).catch(error => {
      console.error("Erro ao sair: ", error);
      alert("Erro ao sair: " + error.message);
    });
  }

// Verifica se o usuário está logado na página de dashboard
if (window.location.pathname.includes('dashboard.html')) {
    if (localStorage.getItem('loggedInUser')) {
        loadDashboard();
    } else {
        window.location.href = 'index.html';
    }
}
