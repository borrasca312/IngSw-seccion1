import { defineStore } from 'pinia'
import { ref } from 'vue'

type AuthUser = {
  full_name?: string
  email?: string
}

export const useAuthStore = defineStore('auth', () => {
  const user = ref<AuthUser | null>(null)
  const token = ref<string | null>(localStorage.getItem('access_token'))
  const loading = ref(false)
  const error = ref<string | null>(null)

  const login = async (
    credsOrUsername: { username: string; password: string } | string,
    password?: string
  ) => {
    loading.value = true
    error.value = null
    try {
      const username = typeof credsOrUsername === 'string' ? credsOrUsername : credsOrUsername.username
      // Mock login (sustituir por llamada real a API cuando esté disponible)
      console.log('Login attempt:', username)
      // Simular login fallido por ahora
      error.value = 'Backend not connected'
      return { success: false, message: error.value }
    } catch (e: any) {
      error.value = e?.message || 'Error de autenticación'
      throw e
    } finally {
      loading.value = false
    }
  }

  const logout = async () => {
    user.value = null
    token.value = null
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  }

  return {
    user,
    token,
    loading,
    error,
    login,
    logout
  }
})