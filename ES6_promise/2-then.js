/* eslint-disable */
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch((error) => {
      throw error; // Throw the error to be consistent with the rejected promise
    })
    .finally(() => console.log('Got a response from the API'));
}
