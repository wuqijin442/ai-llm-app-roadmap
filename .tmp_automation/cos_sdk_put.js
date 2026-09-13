// COS upload via official SDK cos-nodejs-sdk-v5 (matches historical cos-upload.cjs behavior)
const fs = require('fs');
const Cos = require('C:/Users/Administrator/.workbuddy/binaries/node/workspace/node_modules/cos-nodejs-sdk-v5');

function arg(name) {
  const i = process.argv.indexOf('--' + name);
  return i >= 0 ? process.argv[i + 1] : '';
}

const cos = new Cos({
  SecretId: arg('secret-id'),
  SecretKey: arg('secret-key'),
  XCosSecurityToken: arg('token'),
  Protocol: 'https:'
});

cos.putObject(
  {
    Bucket: arg('bucket'),
    Region: arg('region'),
    Key: arg('cos-key'),
    Body: fs.readFileSync(arg('file')),
    ContentType: arg('content-type') || 'text/markdown',
    onProgress: () => {}
  },
  (err, data) => {
    if (err) {
      console.log('COS_UPLOAD_FAIL ' + (err.code || '') + ' ' + (err.message || '').slice(0, 300));
      process.exit(1);
    }
    console.log('COS_UPLOAD_OK ' + (data && data.Location ? data.Location : ''));
    process.exit(0);
  }
);
