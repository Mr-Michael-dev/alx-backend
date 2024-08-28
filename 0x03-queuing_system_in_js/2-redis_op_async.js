// create a connection to node_redis client
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify the get function
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

client.on('ready', async () => {
  console.log('Redis client connected to the server');
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
});
