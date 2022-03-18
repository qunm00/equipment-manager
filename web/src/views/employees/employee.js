const createEmployee = async (employeeData) => {
  console.log('hello')
  fetch('/api/employees', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(employeeData)
  })
  .then(response => console.log(response))
  .catch(error => console.log(error))
}

const editEmployee = async (employeeId, employeeData) => {
  fetch(`/api/employees/${employeeId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(employeeData)
  })
  .then(response => console.log(response))
  .catch(error => console.log(error))
}

const deleteEmployee = async () => {
  fetch(`/api/employees/${employeeId}`, {
    method: 'DELETE',
  })
  .then(response => console.log(response))
  .catch(error => console.log(error))
}

export {
  createEmployee,
  editEmployee,
  deleteEmployee
}