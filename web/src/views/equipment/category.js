import { handleException } from "../../utils"

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
  getCategories,
  getCategoryByName,
  createCategory
}