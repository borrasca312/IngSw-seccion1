import { apiClient } from './api';
import type { Curso } from '@/types/curso';

export const cursoService = {
  getAll(): Promise<Curso[]> {
    return apiClient.get('/cursos/').then(res => res.data);
  },

  getById(id: number): Promise<Curso> {
    return apiClient.get(`/cursos/${id}/`).then(res => res.data);
  },

  create(curso: Partial<Curso>): Promise<Curso> {
    return apiClient.post('/cursos/', curso).then(res => res.data);
  },

  update(id: number, curso: Partial<Curso>): Promise<Curso> {
    return apiClient.put(`/cursos/${id}/`, curso).then(res => res.data);
  },

  delete(id: number): Promise<void> {
    return apiClient.delete(`/cursos/${id}/`);
  },
};
