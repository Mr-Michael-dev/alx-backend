// Create the Job creator using kue
import { createQueue } from 'kue';

const queue = createQueue();

// Job data example
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a test notification',
};

// Create the Job
const job = queue.create('push_notification_code', jobData)
  .attempts(3)
  .save((err) => {
    if (err) {
      console.error('Notification job failed');
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Listen for job completion
job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
