// Node Redis client publisher and subscriber
import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

subscriber.on('ready', () => {
  console.log('Redis client connected to the server');

  subscriber.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
      console.log(message);
      process.exit(0);
    }
    console.log(`${message}`);
  });
  subscriber.subscribe('holberton school channel', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
