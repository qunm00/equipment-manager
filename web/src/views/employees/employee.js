const handleException = (response) => {
  if (!response.ok) {
    throw response
  }
  return response
}

const getEmployees = async () => {
  const employees = await fetch('/api/employees')
  return await employees.json()
}

const getEmployeeByName = async (nickname) => {
  const employee = await fetch(`/api/employees/${nickname}`)
  return await employee.json()
}

const createEmployee = async (employeeData) => {
  const response = await fetch('/api/employees', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(employeeData)
  })
  return handleException(response)
}

const editEmployee = async (employeeId, employeeData) => {
  const response = await fetch(`/api/employees/${employeeId}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(employeeData)
  })
  return handleException(response)

}

const deleteEmployee = async (employeeId) => {
  await fetch(`/api/employees/${employeeId}`, {
    method: 'DELETE',
  })
}

export {
  getEmployees,
  getEmployeeByName,
  createEmployee,
  editEmployee,
  deleteEmployee
}