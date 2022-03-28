const handleException = (response) => {
  if (!response.ok) {
    throw response
  }
  return response
}

export {
  handleException
}