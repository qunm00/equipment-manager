const handleException = (response) => {
  if (!response.ok) {
    throw response
  }
  return response
}

const toggler = (reactiveVar) => {
  reactiveVar.value = !reactiveVar.value
}

export {
  handleException,
  toggler
}

