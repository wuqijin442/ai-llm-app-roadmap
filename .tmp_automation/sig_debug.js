// Try signature variants to diagnose 403 SignatureDoesNotMatch
const crypto = require('crypto');
const secretKey = 'PetUDPV9YDqXHectgqxqDkWnjKXRVsoUDD+ub9nPTX4=';
const keyTime = '1789254984;1789298184';
const cosKey = '5/aDEYK6sCejSmL9VdMN7N4D/file_manager/01a097e864497dc6b795fd6bbc162ac2.md';
const httpString = `put\n/${cosKey}\n\n\n`;
const sha1Http = crypto.createHash('sha1').update(httpString).digest('hex');
console.log('sha1(httpString) =', sha1Http, '(server expects b24cd3a16c5c896b4da4d6e9c4369a02b029fff5)');
const stringToSign = `${sha1Http}\n${keyTime}`;
const skRaw = crypto.createHmac('sha1', secretKey).update(keyTime).digest('hex');
const skB64 = crypto.createHmac('sha1', Buffer.from(secretKey, 'base64')).update(keyTime).digest('hex');
console.log('signKey raw  =', skRaw);
console.log('signKey b64  =', skB64);
console.log('sig raw =', crypto.createHmac('sha1', skRaw).update(stringToSign).digest('hex'));
console.log('sig b64 =', crypto.createHmac('sha1', skB64).update(stringToSign).digest('hex'));
