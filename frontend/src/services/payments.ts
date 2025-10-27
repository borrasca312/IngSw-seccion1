import axios from 'axios'

export interface PaymentItem {
  id: number
  preinscripcion: number
  monto: string | number
  medio: string
  referencia: string
  notas: string
  estado: string
  fecha_pago: string | null
  created_at: string
  updated_at: string
}

export interface PaymentsByGroupResponse {
  group: string
  count: number
  total_amount: string
  breakdown: Record<string, number>
  items: PaymentItem[]
}

export async function getPaymentsByGroup(
  group: string,
  courseId?: number,
  signal?: AbortSignal
): Promise<PaymentsByGroupResponse & { totalAmount: number }> {
  const params: Record<string, any> = { group }
  if (courseId != null) {
    params.course = courseId
  }
  const { data } = await axios.get<PaymentsByGroupResponse>(
    '/api/payments/by-group/',
    { params, signal }
  )
  const totalAmount = Number(data.total_amount as unknown as string)
  return { ...data, totalAmount }
}

export async function getPayment(id: number) {
  const { data } = await axios.get(`/api/payments/pagos-persona/${id}/`)
  return data
}

export async function createPayment(payload: Record<string, any>) {
  const { data } = await axios.post('/api/payments/pagos-persona/', payload)
  return data
}

export async function updatePayment(id: number, payload: Record<string, any>) {
  const { data } = await axios.put(`/api/payments/pagos-persona/${id}/`, payload)
  return data
}

export async function deletePayment(id: number) {
  const { data } = await axios.delete(`/api/payments/pagos-persona/${id}/`)
  return data
}

// Comprobante related
export async function createComprobante(payload: Record<string, any>) {
  const { data } = await axios.post('/api/payments/comprobantes-pago/', payload)
  return data
}

// Cambio titularidad
export async function changeTitularidad(payload: Record<string, any>) {
  const { data } = await axios.post('/api/payments/pagos-cambio-persona/', payload)
  return data
}

export default {
  getPaymentsByGroup,
  getPayment,
  createPayment,
  updatePayment,
  deletePayment,
  createComprobante,
  changeTitularidad
}
