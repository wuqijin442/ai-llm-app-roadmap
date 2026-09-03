const fs = require('fs');
const path = require('path');

async function uploadToCOS(filePath, cosKey, credentials) {
  const { secret_id, secret_key, region, bucket_name, custom_domain, token } = credentials;
  const fileContent = fs.readFileSync(filePath);
  
  // Use COS SDK via Node.js
  try {
    const COS = require('cos-nodejs-sdk-v5');
    const cos = new COS({
      SecretId: secret_id,
      SecretKey: secret_key,
      Protocol: 'https:',
      ...(token ? { SecurityToken: token } : {})
    });
    
    return new Promise((resolve, reject) => {
      cos.putObject({
        Bucket: bucket_name,
        Region: region,
        Key: cosKey,
        Body: fileContent,
        ContentType: 'text/markdown',
        Callback: JSON.stringify({
          status_code: 200,
          success_status_code: 'include',
          timeout: 5,
          callback_url: 'https://ima.qq.com/api/upload/callback'
        })
      }, (err, data) => {
        if (err) reject(err);
        else resolve(data);
      });
    });
  } catch (e) {
    // Fallback to raw HTTP PUT with signed URL
    const crypto = require('crypto');
    
    // Build signed URL
    const method = 'PUT';
    const url = `https://${custom_domain}/${cosKey}`;
    const timestamp = Math.floor(Date.now() / 1000);
    const expire = 3600;
    const xCosDate = new Date(timestamp * 1000).toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, '');
    
    const keyTime = `${timestamp}-${timestamp + expire}`;
    const httpString = `${method}\n/${cosKey}\n?\n${secret_id}\n${keyTime}`;
    const signature = crypto.createHash('sha1').update(httpString).digest('hex');
    
    const auth = `q-sign-algorithm=sha1&q-ak=${secret_id}&q-sign-time=${keyTime}&q-key-time=${keyTime}&q-header-list=&q-url-param-list=&q-signature=${signature}`;
    
    const https = require('https');
    const urlObj = new URL(url);
    
    return new Promise((resolve, reject) => {
      const req = https.request({
        hostname: urlObj.hostname,
        path: urlObj.pathname + '?sign=' + encodeURIComponent(auth),
        method: 'PUT',
        headers: {
          'Content-Type': 'text/markdown',
          'Content-Length': fileContent.length,
          'Authorization': auth
        }
      }, (res) => {
        let data = '';
        res.on('data', (chunk) => data += chunk);
        res.on('end', () => {
          if (res.statusCode >= 200 && res.statusCode < 300) resolve(data);
          else reject(new Error(`HTTP ${res.statusCode}: ${data}`));
        });
      });
      req.on('error', reject);
      req.write(fileContent);
      req.end();
    });
  }
}

const filePath = process.argv[2];
const cosKey = process.argv[3];
const credJson = process.argv[4];
const credentials = JSON.parse(credJson);

uploadToCOS(filePath, cosKey, credentials)
  .then((result) => {
    console.log('UPLOAD_OK');
    console.log(JSON.stringify(result));
  })
  .catch((err) => {
    console.error('UPLOAD_FAILED');
    console.error(err.message);
    process.exit(1);
  });
