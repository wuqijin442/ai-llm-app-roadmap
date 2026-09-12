const fs = require('fs');
const path = require('path');
const roots = [
  'C:/Users/Administrator/.workbuddy',
  'C:/Users/Administrator/.workbuddy/project-resources',
  'C:/Users/Administrator/.workbuddy/connectors',
  'E:/Ksoftware/WorkBuddy/resources/app.asar.unpacked/resources/plugins'
];
const found = [];
function walk(dir, depth) {
  if (depth > 8 || found.length > 5) return;
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch (x) { return; }
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walk(full, depth + 1);
    else if (e.name === 'cos-upload.cjs') found.push(full);
  }
}
for (const r of roots) walk(r, 0);
console.log(found.length ? found.join('\n') : 'NOT FOUND');
