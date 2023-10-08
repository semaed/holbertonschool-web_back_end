/* eslint-disable */
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch((error) => Promise.reject(error)) // Return a rejected promise with the error
    .finally(() => console.log('Got a response from the API'));
}
