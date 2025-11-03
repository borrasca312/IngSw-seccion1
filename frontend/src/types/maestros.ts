export interface Region {
  id: number;
  descripcion: string;
}

export interface Provincia {
  id: number;
  descripcion: string;
  region: number;
}

export interface Comuna {
  id: number;
  descripcion: string;
  provincia: number;
}

export interface Cargo {
  id: number;
  descripcion: string;
}

export interface TipoCurso {
  id: number;
  descripcion: string;
}

// Add other maestro types as needed...
