import { handleException } from "../../utils"

const getEmployees = async () => {
  const employees = await fetch('/api/employees')
  return await employees.json()
}

const getEmployeesCount = async () => {
  const count = await fetch('/api/employees/count')
  return await count.json()
}

const getEmployeeByName = async (nickname) => {
  const employee = await fetch(`/api/employees/${nickname}`)
  return await employee.json()
}

const createEmployee = async (employeeData) => {
  console.log(employeeData)
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
  const response = await fetch(`/api/employees/${employeeId}`, {
    method: 'DELETE',
  })
  return handleException(response)
}

const filterEmployees = (employees, searchTerm) => {
  if (searchTerm.length === 0) {
    return employees
  }
  return employees.filter(employee => {
    return employee.email.toLowerCase().includes(searchTerm)
      || employee.fullname.toLowerCase().includes(searchTerm)
      || employee.mobile.toLowerCase().includes(searchTerm)
      || employee.nickname.toLowerCase().includes(searchTerm)
  })
}

export {
  getEmployees,
  getEmployeeByName,
  getEmployeesCount,
  createEmployee,
  editEmployee,
  deleteEmployee,
  filterEmployees
}