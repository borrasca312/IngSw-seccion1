import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as paymentsService from '@/services/payments'
import type { Payment } from '@/types'

interface Meta {
  count: number
  totalAmount: number
  breakdown: Record<string, any>
}

export const usePaymentsStore = defineStore('payments', () => {
  const list = ref<Payment[]>([])
  const meta = ref<Meta>({ count: 0, totalAmount: 0, breakdown: {} })
  const loading = ref(false)
  const error = ref<string | null>(null)

  async function fetchByGroup(group: string, courseId?: number) {
    loading.value = true
    error.value = null
    try {
      const data = await paymentsService.getPaymentsByGroup(group, courseId)
      list.value = data.items
      meta.value = {
        count: data.count,
        totalAmount: parseFloat(data.total_amount) || 0,
        breakdown: data.breakdown
      }
      return data
    } catch (err: any) {
      error.value = err?.message || 'Error cargando pagos'
      throw err
    } finally {
      loading.value = false
    }
  }

  async function get(id: number) {
    loading.value = true
    try {
      const data = await paymentsService.getPayment(id)
      return data
    } finally {
      loading.value = false
    }
  }

  async function create(payload: Record<string, any>) {
    loading.value = true
    try {
      const data = await paymentsService.createPayment(payload)
      return data
    } finally {
      loading.value = false
    }
  }

  async function update(id: number, payload: Record<string, any>) {
    loading.value = true
    try {
      const data = await paymentsService.updatePayment(id, payload)
      return data
    } finally {
      loading.value = false
    }
  }

  async function remove(id: number) {
    loading.value = true
    try {
      const data = await paymentsService.deletePayment(id)
      return data
    } finally {
      loading.value = false
    }
  }

  async function emitirComprobante(payload: Record<string, any>) {
    loading.value = true
    try {
      const data = await paymentsService.createComprobante(payload)
      return data
    } finally {
      loading.value = false
    }
  }

  async function cambioTitularidad(payload: Record<string, any>) {
    loading.value = true
    try {
      const data = await paymentsService.changeTitularidad(payload)
      return data
    } finally {
      loading.value = false
    }
  }

  return {
    // state
    list,
    meta,
    loading,
    error,

    // actions
    fetchByGroup,
    get,
    create,
    update,
    remove,
    emitirComprobante,
    cambioTitularidad
  }
})
