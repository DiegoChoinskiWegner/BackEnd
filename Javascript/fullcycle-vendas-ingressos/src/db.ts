import { Client } from 'pg';
import { readFileSync } from 'fs';
import { google } from 'googleapis';

// Load credentials from JSON keyfile
const keyFilePath = './path/to/your-service-account-key.json'; // Replace with your path
const credentials = JSON.parse(readFileSync(keyFilePath, 'utf-8'));

const dbConfig = {
  user: 'your-postgres-username',
  host: 'your-cloud-sql-instance-ip',
  database: 'your-database-name',
  password: 'your-postgres-password',
  port: 5432,
};

(async () => {
  const client = new Client(dbConfig);

  try {
    // Connect to the database
    await client.connect();
    console.log('Connected to the database successfully.');

    // Create tables for partners, customers, events, and tickets
    const tables = [
      { name: 'partners', query: 'CREATE TABLE IF NOT EXISTS partners (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);' },
      { name: 'customers', query: 'CREATE TABLE IF NOT EXISTS customers (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);' },
      { name: 'events', query: 'CREATE TABLE IF NOT EXISTS events (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);' },
      { name: 'tickets', query: 'CREATE TABLE IF NOT EXISTS tickets (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);' },
    ];

    for (const table of tables) {
      await client.query(table.query);
      console.log(`Table '${table.name}' created successfully.`);
    }
  } catch (err) {
    console.error('Error connecting to the database or creating tables:', err);
  } finally {
    await client.end();
  }
})();
