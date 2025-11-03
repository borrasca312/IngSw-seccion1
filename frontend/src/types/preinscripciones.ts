export interface Preinscripcion {
  id: number;
  user: number;
  user_name: string;
  user_email: string;
  course: number;
  course_title: string;
  course_code: string;
  estado: string;
  estado_display: string;
  grupo: string;
  puede_pagar: boolean;
  created_at: string;
  updated_at: string;
}
