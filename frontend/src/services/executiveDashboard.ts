import apiClient from './api';

export interface CursoActivo {
  id: number;
  nombre: string;
  fecha_inicio: string;
  fecha_fin: string;
  estado: 'Activo' | 'Finalizando' | 'Completado' | 'Cancelado';
  participantes_actuales: number;
  participantes_max: number;
  instructor: string;
}

export interface ExecutiveMetrics {
  cursosActivos: number;
  totalParticipantes: number;
  ingresosMes: number;
  tasaCompletitud: number;
  participantesPorRama: Array<{ nombre: string; num_participantes: number }>;
  ingresosMensuales: Array<{ mes: string; ingresos: number }>;
}

export const getExecutiveMetrics = async (period: string = 'month'): Promise<ExecutiveMetrics> => {
  try {
    const response = await apiClient.get(`/dashboard/executive-metrics/?period=${period}`);
    return response.data;
  } catch (error) {
    //Datos de respaldo para desarrollo
    return {
      cursosActivos: 12,
      totalParticipantes: 245,
      ingresosMes: 1250000,
      tasaCompletitud: 87,
      participantesPorRama: [
        { nombre: 'Lobatos', num_participantes: 45 },
        { nombre: 'Scouts', num_participantes: 78 },
        { nombre: 'Pioneros', num_participantes: 65 },
        { nombre: 'Rovers', num_participantes: 57 }
      ],
      ingresosMensuales: [
        { mes: 'Enero', ingresos: 800000 },
        { mes: 'Febrero', ingresos: 950000 },
        { mes: 'Marzo', ingresos: 1100000 },
        { mes: 'Abril', ingresos: 1250000 },
        { mes: 'Mayo', ingresos: 1180000 },
        { mes: 'Junio', ingresos: 1350000 }
      ]
    };
  }
};

export const getCursosActivos = async (): Promise<CursoActivo[]> => {
  try {
    const response = await apiClient.get('/cursos/activos/');
    return response.data;
  } catch (error) {
    //Datos de respaldo para desarrollo
    return [
      {
        id: 1,
        nombre: 'Curso de Liderazgo Scout',
        fecha_inicio: '2024-01-15',
        fecha_fin: '2024-03-15',
        estado: 'Activo',
        participantes_actuales: 18,
        participantes_max: 25,
        instructor: 'Juan Pérez'
      },
      {
        id: 2,
        nombre: 'Técnicas de Campamento',
        fecha_inicio: '2024-02-01',
        fecha_fin: '2024-04-01',
        estado: 'Activo',
        participantes_actuales: 22,
        participantes_max: 30,
        instructor: 'María González'
      },
      {
        id: 3,
        nombre: 'Primeros Auxilios Básicos',
        fecha_inicio: '2024-01-20',
        fecha_fin: '2024-02-20',
        estado: 'Finalizando',
        participantes_actuales: 15,
        participantes_max: 20,
        instructor: 'Carlos Ruiz'
      }
    ];
  }
};