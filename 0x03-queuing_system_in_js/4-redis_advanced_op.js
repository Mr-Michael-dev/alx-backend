// create a connection to node_redis client
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify the hgetall function
const hGetAllAsync = promisify(client.hgetall).bind(client);

const hashValue = {
  'Portland': '50',
  'Seattle': '80',
  'New York': '20',
  'Bogota': '20',
  'Cali': '40',
  'Paris': '2'
}


async function displayHashValue(hashName) {
  try {
    const value = await hGetAllAsync(hashName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

client.on('ready', async () => {
  console.log('Redis client connected to the server');
  await client.hset('HolbertonSchools', hashValue, print);
  await displayHashValue('HolbertonSchools');
});
