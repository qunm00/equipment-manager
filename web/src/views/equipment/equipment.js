import { handleException } from "../../utils"

const getEquipment = async () => {
  const equipment = await fetch('/api/equipment')
  return await equipment.json()
}

const getEquipmentCount = async () => {
  const count = await fetch('/api/equipment/count')
  return await count.json()
}

const getEquipmentAvailabilityCount = async () => {
  const availability_count = await fetch('/api/equipment/availability-count')
  return await availability_count.json()
}

const createDevice = async (deviceData) => {
  const response = await fetch('/api/equipment', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body:  JSON.stringify(deviceData)
  })
  return handleException(response)
}

const editDevice = async (deviceData) => {
  const response = await fetch(`/api/equipment/${deviceData.id}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body:  JSON.stringify(deviceData)
  })
  return handleException(response)
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
  const response = await fetch('/api/categories', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'category': newCategory
    })
  })
  return handleException(response)
}

export {
  getEquipment,
  getEquipmentCount,
  getEquipmentAvailabilityCount,
  createDevice,
  editDevice,
  deleteDevice,
  getCategories,
  getCategoryByName,
  createCategory
}