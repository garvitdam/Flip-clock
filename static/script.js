const hoursNode = document.getElementById('hours');
const minutesNode = document.getElementById('minutes');
const secondsNode = document.getElementById('seconds');
const weekdayNode = document.getElementById('weekday');
const dateTextNode = document.getElementById('date-text');
const timezoneNameNode = document.getElementById('timezone-name');
const timezoneFlagNode = document.getElementById('timezone-flag');

function formatPart(value) {
  return String(value).padStart(2, '0');
}

function updateClock() {
  const now = new Date();

  hoursNode.textContent = formatPart(now.getHours());
  minutesNode.textContent = formatPart(now.getMinutes());
  secondsNode.textContent = formatPart(now.getSeconds());

  weekdayNode.textContent = now.toLocaleDateString('en-US', { weekday: 'long' });
  dateTextNode.textContent = now.toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  });

  const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC';
  timezoneNameNode.textContent = timezone.replace(/_/g, ' ');
  timezoneFlagNode.textContent = timezone.includes('/') ? timezone.split('/').pop() : timezone;
}

updateClock();
setInterval(updateClock, 1000);
