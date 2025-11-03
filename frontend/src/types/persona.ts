export interface Persona {
  id: number;
  run: string;
  dv: string;
  nombres: string;
  apellido_paterno: string;
  apellido_materno: string;
  email: string;
  fecha_nacimiento: string;
  direccion: string;
  tipo_fono: number;
  telefono: string;
  comuna: { id: number; descripcion: string };
  estado_civil: { id: number; descripcion: string };
}
