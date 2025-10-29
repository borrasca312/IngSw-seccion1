export interface Curso {
  id: number;
  tipo_curso: { id: number; descripcion: string };
  responsable: { id: number; nombres: string; apellido_paterno: string };
  cargo_responsable: { id: number; descripcion: string };
  lugar_comuna: { id: number; descripcion: string } | null;
  fecha_hora: string;
  fecha_solicitud: string;
  codigo: string;
  descripcion: string;
  observacion: string;
  administra: number;
  cuota_con_almuerzo: number;
  cuota_sin_almuerzo: number;
  modalidad: number;
  lugar: string;
  estado: number;
  usuario: { id: number; username: string };
  coordinadores: any[];
  cuotas: any[];
  fechas: any[];
  secciones: any[];
  formadores: any[];
  alimentacion: any[];
  participantes: { id: number; persona: { nombres: string; apellido_paterno: string }; acreditado: boolean }[];
  total_participantes: number;
  total_formadores: number;
  monto_recaudado: number;
}
