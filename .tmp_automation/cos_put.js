// COS XML API PUT with temporary credentials (sha1 signature), no SDK dependency.
// Usage: node cos_put.js --file <path> --secret-id <id> --secret-key <key> --token <token> --bucket <b> --region <r> --cos-key <k> --content-type <ct> --start-time <s> --expired-time <e>
const fs = require('fs');
const crypto = require('crypto');

function arg(name) {
  const i = process.argv.indexOf('--' + name);
  return i >= 0 ? process.argv[i + 1] : '';
}

(async () => {
  const file = arg('file');
  const secretId = arg('secret-id');
  const secretKey = arg('secret-key');
  const token = arg('token');
  const bucket = arg('bucket');
  const region = arg('region');
  const cosKey = arg('cos-key');
  const contentType = arg('content-type') || 'text/markdown';
  const startTime = arg('start-time');
  const expiredTime = arg('expired-time');

  const body = fs.readFileSync(file);
  const url = `https://${bucket}.cos.${region}.myqcloud.com/${cosKey}`;
  const keyTime = `${startTime};${expiredTime}`;
  const sigMode = arg('sig-mode') || 'raw';
  const hmacKey = sigMode === 'b64' ? Buffer.from(secretKey, 'base64') : secretKey;

  const signKey = crypto.createHmac('sha1', hmacKey).update(keyTime).digest('hex');
  const httpString = `put\n/${cosKey}\n\n\n`;
  const sha1Http = crypto.createHash('sha1').update(httpString).digest('hex');
  const stsOrder = arg('sts-order') || 'doc'; // doc: sha1\nhash\nkeyTime ; srv: sha1\nkeyTime\nhash
  const stringToSign = stsOrder === 'srv'
    ? `sha1\n${keyTime}\n${sha1Http}`
    : `sha1\n${sha1Http}\n${keyTime}`;
  const signature = crypto.createHmac('sha1', signKey).update(stringToSign).digest('hex');
  const authorization =
    `q-sign-algorithm=sha1&q-ak=${secretId}&q-sign-time=${keyTime}` +
    `&q-key-time=${keyTime}&q-header-list=&q-url-param-list=&q-signature=${signature}`;

  const res = await fetch(url, {
    method: 'PUT',
    headers: {
      Authorization: authorization,
      'Content-Type': contentType,
      'x-cos-security-token': token
    },
    body
  });
  const text = await res.text();
  console.log(`HTTP ${res.status}`);
  if (res.status >= 200 && res.status < 300) {
    console.log('COS_UPLOAD_OK');
    process.exit(0);
  } else {
    console.log(text.slice(0, 800));
    process.exit(1);
  }
})();
