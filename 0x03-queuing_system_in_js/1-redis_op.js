// create a connection to node_redis client
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

async function setNewSchool(schoolName, value) {
	await client.set(schoolName, value, print);
};

async function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log(value);
    });
};

client.on('ready', async () => {
    console.log('Redis client connected to the server');
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
});
