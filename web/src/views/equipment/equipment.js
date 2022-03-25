const getEquipment = async () => {
  const equipment = await fetch('/api/equipment')
  return await equipment.json()
}

const createDevice = async (deviceData) => {
  await fetch('/api/equipment', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body:  JSON.stringify(deviceData)
  })
}

const editDevice = async (deviceData) => {
  await fetch(`/api/equipment/${deviceData.id}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body:  JSON.stringify(deviceData)
  })
}

const deleteDevice = async (deviceID) => {
  await fetch(`/api/equipment/${deviceID}`, {
    method: 'DELETE'
  })
}

const getCategories = async () => {
  const categories = await fetch('/api/categories')
  return await categories.json()
}

const getCategoryByName = async (category) => {
  const categories = await fetch(`/api/categories/${category}`)
  return await categories.json()
}

const createCategory = async (newCategory) => {
  await fetch('/api/categories', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'category': newCategory
    })
  })
}

export {
  getEquipment,
  createDevice,
  editDevice,
  deleteDevice,
  getCategories,
  getCategoryByName,
  createCategory
}