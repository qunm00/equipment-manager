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

const filterEquipment = (
  equipment,
  selectedCategory,
  selectedEmployee, 
  selectedSerialNumber
) => {
  const matchedCategory = new Set(equipment.filter(device => {
    if (selectedCategory === undefined) {
      return device
    } else {
      return device.category.category === selectedCategory
    }
  }))

  const matchedEmployee = new Set(equipment.filter(device => {
    if (selectedEmployee === undefined) {
      return device
    } else {
      if (device.employee !== null) {
        return device.employee.nickname === selectedEmployee
      }
    }
  }))

  const matchedSerialNumber = new Set(equipment.filter(device => {
    if (selectedSerialNumber === '') {
      return device
    } else {
      return device.serialnumber.toLowerCase().includes(selectedSerialNumber.toLowerCase())
    }
  }))

  const result = new Set([...matchedCategory]
    .filter(device => matchedEmployee.has(device))
    .filter(device => matchedSerialNumber.has(device)))

  return result
}

export {
  getEquipment,
  getEquipmentCount,
  getEquipmentAvailabilityCount,
  createDevice,
  editDevice,
  deleteDevice,
  filterEquipment
}