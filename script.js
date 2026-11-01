const hoursNode = document.getElementById('hours');
const minutesNode = document.getElementById('minutes');
const secondsNode = document.getElementById('seconds');
const weekdayNode = document.getElementById('weekday');
const dateTextNode = document.getElementById('date-text');
const timezoneNameNode = document.getElementById('timezone-name');
const timezoneFlagNode = document.getElementById('timezone-flag');

const localTimeNode = document.getElementById('local-time');
const utcTimeNode = document.getElementById('utc-time');
const tokyoTimeNode = document.getElementById('tokyo-time');
const nyTimeNode = document.getElementById('ny-time');

function formatTimePart(value) {
  return String(value).padStart(2, '0');
}

function updateClock() {
  const now = new Date();

  hoursNode.textContent = formatTimePart(now.getHours());
  minutesNode.textContent = formatTimePart(now.getMinutes());
  secondsNode.textContent = formatTimePart(now.getSeconds());

  weekdayNode.textContent = now.toLocaleDateString('en-US', { weekday: 'long' });
  dateTextNode.textContent = now.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  });

  const localeTime = now.toLocaleTimeString('en-US', {
    timeZoneName: 'short'
  });
  timezoneNameNode.textContent = localeTime;
  timezoneFlagNode.textContent = Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC';

  localTimeNode.textContent = now.toLocaleTimeString('en-US', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  });

  utcTimeNode.textContent = new Date(now.toISOString()).toLocaleTimeString('en-US', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false,
    timeZone: 'UTC'
  });

  tokyoTimeNode.textContent = new Intl.DateTimeFormat('en-US', {
    timeZone: 'Asia/Tokyo',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  }).format(now);

  nyTimeNode.textContent = new Intl.DateTimeFormat('en-US', {
    timeZone: 'America/New_York',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  }).format(now);
}

updateClock();
setInterval(updateClock, 1000);
