export interface Pago {
  id: number;
  persona: number;
  curso: number;
  valor: number;
}

export interface PaymentBreakdown {
  ingresos: number;
  egresos: number;
  pendientes: number;
  registrados: number;
}
