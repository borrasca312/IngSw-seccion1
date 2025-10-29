export interface Curso {
  id: number;
  codigo: string;
  descripcion: string;
  responsable: number;
  cargo_responsable: number;
  comuna: number;
  lugar: string;
  fecha_solicitud: string;
  administra: number;
  cuota_con_almuerzo: number;
  cuota_sin_almuerzo: number;
  modalidad: number;
  tipo_curso: number;
  estado: string;
  fecha_termino: string;
}
