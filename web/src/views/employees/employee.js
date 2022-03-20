const getEmployees = () => {
  return fetch('api/employees')
  .then(response => response.json())
}

const createEmployee = (employeeData) => {
  return fetch('/api/employees', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(employeeData)
  })
  .then(response => console.log(response))
  .catch(error => console.log(error))
}

const editEmployee = (employeeId, employeeData) => {
  return fetch(`/api/employees/${employeeId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(employeeData)
  })
  .then(response => console.log(response))
  .catch(error => console.log(error))
}

const deleteEmployee = (employeeId) => {
  return fetch(`/api/employees/${employeeId}`, {
    method: 'DELETE',
  })
  .then(response => console.log(response))
  .catch(error => console.log(error))
}

export {
  getEmployees,
  createEmployee,
  editEmployee,
  deleteEmployee
}