import React, { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { Button } from '@/components/ui/Button';
import { initializeSampleData } from '@/data/samplePersonas';
import { 
  Plus, 
  Search, 
  Filter, 
  Edit, 
  Trash2, 
  User, 
  Phone, 
  Mail, 
  MapPin,
  Calendar,
  Award,
  ChevronLeft,
  Eye,
  Clock
} from 'lucide-react';

const PersonasPage = () => {
  const navigate = useNavigate();
  const [personas, setPersonas] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredPersonas, setFilteredPersonas] = useState([]);
  const [showFilters, setShowFilters] = useState(false);
  const [selectedPersona, setSelectedPersona] = useState(null);
  const [showModal, setShowModal] = useState(false);

  // Cargar personas desde localStorage (simulación)
  useEffect(() => {
    const storedPersonas = initializeSampleData();
    setPersonas(storedPersonas);
    setFilteredPersonas(storedPersonas);
  }, []);

  // Filtrar personas por término de búsqueda
  useEffect(() => {
    const filtered = personas.filter(persona =>
      `${persona.nombres} ${persona.apellidoPaterno} ${persona.apellidoMaterno}`
        .toLowerCase()
        .includes(searchTerm.toLowerCase()) ||
      persona.rut?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      persona.email?.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredPersonas(filtered);
  }, [searchTerm, personas]);

  const handleEditPersona = (id) => {
    navigate(`/personas/editar/${id}`);
  };

  const handleViewPersona = (persona) => {
    setSelectedPersona(persona);
    setShowModal(true);
  };

  const handleDeletePersona = (id) => {
    if (window.confirm('¿Está seguro de que desea eliminar esta persona?')) {
      const updatedPersonas = personas.filter(p => p.id !== id);
      setPersonas(updatedPersonas);
      localStorage.setItem('personas', JSON.stringify(updatedPersonas));
    }
  };

  return (
    <>
      <Helmet>
        <title>Gestión de Personas - Scout Formación</title>
        <meta name="description" content="Gestión CRUD de personas registradas - Ver, modificar y eliminar registros." />
      </Helmet>

      <div className="min-h-screen bg-gray-50">
        {/* Header */}
        <div className="bg-scout-azul-oscuro text-white shadow-lg">
          <div className="container mx-auto px-4 py-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-4">
                <Button
                  variant="ghost"
                  onClick={() => navigate('/dashboard')}
                  className="text-white hover:bg-scout-azul-medio"
                >
                  <ChevronLeft className="w-5 h-5 mr-2" />
                  Volver
                </Button>
                <div>
                  <div className="flex items-center space-x-3">
                    <User className="w-8 h-8" />
                    <h1 className="text-2xl font-bold">Gestión de Personas</h1>
                  </div>
                  <p className="text-white/80 text-sm mt-1">
                    Ver, modificar y eliminar personas registradas
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Search and Filters */}
        <div className="container mx-auto px-4 py-6">
          <div className="bg-white rounded-lg shadow-md p-6 mb-6">
            <div className="flex flex-col md:flex-row gap-4 items-center">
              <div className="flex-1 relative">
                <Search className="w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
                <input
                  type="text"
                  placeholder="Buscar por nombre, RUT o email..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-scout-azul-medio focus:border-scout-azul-medio transition-colors"
                />
              </div>
              <Button
                variant="outline"
                onClick={() => setShowFilters(!showFilters)}
                className="border-scout-azul-medio text-scout-azul-medio hover:bg-scout-azul-muy-claro"
              >
                <Filter className="w-5 h-5 mr-2" />
                Filtros
              </Button>
            </div>

            {showFilters && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                exit={{ opacity: 0, height: 0 }}
                className="mt-4 pt-4 border-t border-gray-200"
              >
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <select className="input-scout">
                    <option value="">Todas las comunas</option>
                    <option value="santiago">Santiago</option>
                    <option value="providencia">Providencia</option>
                    <option value="las-condes">Las Condes</option>
                  </select>
                  <select className="input-scout">
                    <option value="">Todos los estados civiles</option>
                    <option value="soltero">Soltero/a</option>
                    <option value="casado">Casado/a</option>
                    <option value="divorciado">Divorciado/a</option>
                  </select>
                  <select className="input-scout">
                    <option value="">Estado</option>
                    <option value="activo">Activo</option>
                    <option value="inactivo">Inactivo</option>
                  </select>
                </div>
              </motion.div>
            )}
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="flex items-center">
                <div className="w-12 h-12 bg-scout-azul-muy-claro rounded-lg flex items-center justify-center">
                  <User className="w-6 h-6 text-scout-azul-medio" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">Total Personas</p>
                  <p className="text-2xl font-bold text-scout-azul-oscuro">{personas.length}</p>
                </div>
              </div>
            </div>
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="flex items-center">
                <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                  <Award className="w-6 h-6 text-green-600" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">Formadores</p>
                  <p className="text-2xl font-bold text-scout-azul-oscuro">
                    {personas.filter(p => p.esFormador).length}
                  </p>
                </div>
              </div>
            </div>
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="flex items-center">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                  <Calendar className="w-6 h-6 text-blue-600" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">Nuevos este mes</p>
                  <p className="text-2xl font-bold text-scout-azul-oscuro">
                    {personas.filter(p => {
                      const fechaCreacion = new Date(p.fechaCreacion);
                      const ahora = new Date();
                      return fechaCreacion.getMonth() === ahora.getMonth() && 
                             fechaCreacion.getFullYear() === ahora.getFullYear();
                    }).length}
                  </p>
                </div>
              </div>
            </div>
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="flex items-center">
                <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                  <MapPin className="w-6 h-6 text-purple-600" />
                </div>
                <div className="ml-4">
                  <p className="text-sm font-medium text-gray-600">Activos</p>
                  <p className="text-2xl font-bold text-scout-azul-oscuro">
                    {personas.filter(p => p.vigente).length}
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Personas List */}
          <div className="bg-white rounded-lg shadow-md">
            <div className="p-6 border-b border-gray-200">
              <h2 className="text-xl font-semibold text-scout-azul-oscuro">
                Lista de Personas ({filteredPersonas.length})
              </h2>
            </div>
            
            {filteredPersonas.length === 0 ? (
              <div className="p-12 text-center">
                <User className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900 mb-2">No hay personas registradas</h3>
                <p className="text-gray-500 mb-4">Las personas se registran a través del proceso de preinscripción.</p>
                <Button 
                  onClick={() => navigate('/preinscripcion')}
                  className="bg-scout-azul-medio hover:bg-scout-azul-oscuro"
                >
                  <Plus className="w-5 h-5 mr-2" />
                  Ir a Preinscripción
                </Button>
              </div>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Persona
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Contacto
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Profesión/Religión
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Experiencia Scout
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Estado
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Acciones
                      </th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {filteredPersonas.map((persona, index) => (
                      <motion.tr 
                        key={persona.id || index}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.3, delay: index * 0.1 }}
                        className="hover:bg-gray-50"
                      >
                        <td className="px-6 py-4 whitespace-nowrap">
                          <div className="flex items-center">
                            <div className="w-10 h-10 bg-scout-azul-muy-claro rounded-full flex items-center justify-center">
                              <User className="w-5 h-5 text-scout-azul-medio" />
                            </div>
                            <div className="ml-4">
                              <div className="text-sm font-medium text-gray-900">
                                {persona.nombres} {persona.apellidoPaterno} {persona.apellidoMaterno}
                              </div>
                              <div className="text-sm text-gray-500">
                                {persona.rut}-{persona.dv}
                              </div>
                            </div>
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <div className="text-sm text-gray-900 flex items-center">
                            <Mail className="w-4 h-4 mr-2 text-gray-400" />
                            {persona.email}
                          </div>
                          <div className="text-sm text-gray-500 flex items-center mt-1">
                            <Phone className="w-4 h-4 mr-2 text-gray-400" />
                            {persona.telefono}
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <div className="text-sm text-gray-900">
                            {persona.profesion || 'No especificada'}
                          </div>
                          <div className="text-sm text-gray-500">
                            {persona.religion || 'No especificada'}
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <div className="text-sm text-gray-900">
                            MMAA: {persona.numeroMMAA || 'N/A'}
                          </div>
                          <div className="text-sm text-gray-500">
                            NNAJ: {persona.tiempoNNAJ || 'N/A'}
                          </div>
                          <div className="text-sm text-gray-500">
                            Adultos: {persona.tiempoAdulto || 'N/A'}
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${
                            persona.vigente ? 
                            'bg-green-100 text-green-800' : 
                            'bg-red-100 text-red-800'
                          }`}>
                            {persona.vigente ? 'Activo' : 'Inactivo'}
                          </span>
                          {persona.esFormador && (
                            <span className="inline-flex px-2 py-1 text-xs font-semibold rounded-full bg-purple-100 text-purple-800 ml-2">
                              Formador
                            </span>
                          )}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                          <div className="flex space-x-2">
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => handleViewPersona(persona)}
                              className="text-blue-600 hover:text-blue-800"
                              title="Ver detalles"
                            >
                              <Eye className="w-4 h-4" />
                            </Button>
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => handleEditPersona(persona.id)}
                              className="text-scout-azul-medio hover:text-scout-azul-oscuro"
                              title="Editar"
                            >
                              <Edit className="w-4 h-4" />
                            </Button>
                            <Button
                              variant="ghost"
                              size="sm"
                              onClick={() => handleDeletePersona(persona.id)}
                              className="text-red-600 hover:text-red-800"
                              title="Eliminar"
                            >
                              <Trash2 className="w-4 h-4" />
                            </Button>
                          </div>
                        </td>
                      </motion.tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Modal de Detalles */}
      {showModal && selectedPersona && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            className="bg-white rounded-lg shadow-xl max-w-4xl w-full max-h-[90vh] overflow-y-auto"
          >
            <div className="p-6 border-b border-gray-200">
              <div className="flex items-center justify-between">
                <h2 className="text-2xl font-bold text-scout-azul-oscuro">
                  Detalles de {selectedPersona.nombres} {selectedPersona.apellidoPaterno}
                </h2>
                <Button
                  variant="ghost"
                  onClick={() => setShowModal(false)}
                  className="text-gray-400 hover:text-gray-600"
                >
                  ✕
                </Button>
              </div>
            </div>
            
            <div className="p-6 space-y-6">
              {/* Información Personal */}
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                  <User className="w-5 h-5 mr-2" />
                  Información Personal
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <p className="text-sm font-medium text-gray-600">Nombre Completo</p>
                    <p className="text-sm text-gray-900">{selectedPersona.nombres} {selectedPersona.apellidoPaterno} {selectedPersona.apellidoMaterno}</p>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-gray-600">RUT</p>
                    <p className="text-sm text-gray-900">{selectedPersona.rut}-{selectedPersona.dv}</p>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-gray-600">Fecha de Nacimiento</p>
                    <p className="text-sm text-gray-900">{selectedPersona.fechaNacimiento || 'No especificada'}</p>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-gray-600">Apodo Scout</p>
                    <p className="text-sm text-gray-900">{selectedPersona.apodo || 'No especificado'}</p>
                  </div>
                </div>
              </div>

              {/* Información de Contacto */}
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                  <Phone className="w-5 h-5 mr-2" />
                  Información de Contacto
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <p className="text-sm font-medium text-gray-600">Email</p>
                    <p className="text-sm text-gray-900">{selectedPersona.email}</p>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-gray-600">Teléfono</p>
                    <p className="text-sm text-gray-900">{selectedPersona.telefono}</p>
                  </div>
                  <div className="md:col-span-2">
                    <p className="text-sm font-medium text-gray-600">Dirección</p>
                    <p className="text-sm text-gray-900">{selectedPersona.direccion || 'No especificada'}</p>
                  </div>
                </div>
              </div>

              {/* Información Profesional y Religiosa */}
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                  <Award className="w-5 h-5 mr-2" />
                  Información Adicional
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div>
                    <p className="text-sm font-medium text-gray-600">Profesión</p>
                    <p className="text-sm text-gray-900">{selectedPersona.profesion || 'No especificada'}</p>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-gray-600">Religión</p>
                    <p className="text-sm text-gray-900">{selectedPersona.religion || 'No especificada'}</p>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-gray-600">Número MMAA</p>
                    <p className="text-sm text-gray-900">{selectedPersona.numeroMMAA || 'No asignado'}</p>
                  </div>
                </div>
              </div>

              {/* Experiencia Scout */}
              <div>
                <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                  <Clock className="w-5 h-5 mr-2" />
                  Experiencia Scout
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <p className="text-sm font-medium text-gray-600">Tiempo trabajo con NNAJ</p>
                    <p className="text-sm text-gray-900">{selectedPersona.tiempoNNAJ || 'No especificado'}</p>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-gray-600">Tiempo trabajo con Adultos</p>
                    <p className="text-sm text-gray-900">{selectedPersona.tiempoAdulto || 'No especificado'}</p>
                  </div>
                </div>
              </div>

              {/* Información Médica y Emergencia */}
              {(selectedPersona.alergiasEnfermedades || selectedPersona.nombreEmergencia) && (
                <div>
                  <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                    <Calendar className="w-5 h-5 mr-2" />
                    Información Médica y Emergencia
                  </h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {selectedPersona.alergiasEnfermedades && (
                      <div>
                        <p className="text-sm font-medium text-gray-600">Alergias y Enfermedades</p>
                        <p className="text-sm text-gray-900">{selectedPersona.alergiasEnfermedades}</p>
                      </div>
                    )}
                    {selectedPersona.nombreEmergencia && (
                      <div>
                        <p className="text-sm font-medium text-gray-600">Contacto de Emergencia</p>
                        <p className="text-sm text-gray-900">{selectedPersona.nombreEmergencia}</p>
                        {selectedPersona.telefonoEmergencia && (
                          <p className="text-sm text-gray-500">{selectedPersona.telefonoEmergencia}</p>
                        )}
                      </div>
                    )}
                  </div>
                </div>
              )}

              {/* Estado del Formador */}
              {selectedPersona.esFormador && (
                <div>
                  <h3 className="text-lg font-semibold text-gray-900 mb-4 flex items-center">
                    <Award className="w-5 h-5 mr-2" />
                    Estado como Formador
                  </h3>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                      <p className="text-sm font-medium text-gray-600">Habilitación 1</p>
                      <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${
                        selectedPersona.habilitacion1 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                      }`}>
                        {selectedPersona.habilitacion1 ? 'Completada' : 'Pendiente'}
                      </span>
                    </div>
                    <div>
                      <p className="text-sm font-medium text-gray-600">Habilitación 2</p>
                      <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${
                        selectedPersona.habilitacion2 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                      }`}>
                        {selectedPersona.habilitacion2 ? 'Completada' : 'Pendiente'}
                      </span>
                    </div>
                    <div>
                      <p className="text-sm font-medium text-gray-600">Verificación</p>
                      <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${
                        selectedPersona.verificacion ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'
                      }`}>
                        {selectedPersona.verificacion ? 'Verificado' : 'Sin verificar'}
                      </span>
                    </div>
                  </div>
                </div>
              )}
            </div>

            <div className="p-6 border-t border-gray-200 flex justify-end space-x-4">
              <Button
                variant="outline"
                onClick={() => setShowModal(false)}
                className="border-gray-300 text-gray-700 hover:bg-gray-50"
              >
                Cerrar
              </Button>
              <Button
                onClick={() => {
                  setShowModal(false);
                  handleEditPersona(selectedPersona.id);
                }}
                className="bg-scout-azul-medio hover:bg-scout-azul-oscuro"
              >
                <Edit className="w-4 h-4 mr-2" />
                Editar Persona
              </Button>
            </div>
          </motion.div>
        </div>
      )}
    </>
  );
};

export default PersonasPage;