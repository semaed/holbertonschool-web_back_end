/* eslint-disable */
export default function signUpUser(firstName, lastName) {
  return new Promise((resolve, reject) => {
    if (typeof firstName === 'string' && typeof lastName === 'string') {
      resolve({
        status: 200,
        body: 'success',
      });
    } else {
      reject(new Error('Invalid input'));
    }
  });
}
