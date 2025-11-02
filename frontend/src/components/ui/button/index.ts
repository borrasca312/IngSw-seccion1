import { cva, type VariantProps } from 'class-variance-authority'

// Esta es la lógica que define los estilos del botón
export const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        // Variante Primaria (Azul - para "Crear", "Siguiente")
        primary:
          'bg-blue-600 text-white hover:bg-blue-700',

        // Variante de Éxito (Verde - para "Añadir Widget")
        success:
          'bg-green-600 text-white hover:bg-green-700',

        // Variante Secundaria (Gris/Blanco - para "Cancelar", "Anterior")
        secondary:
          'bg-white text-blue-600 border border-blue-600 hover:bg-blue-50',

        // Variante por defecto (la que ya estaba)
        default:
          'bg-gray-900 text-white hover:bg-gray-800',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
)

// ESTA LÍNEA ES LA MÁS IMPORTANTE PARA ARREGLAR TU ERROR
export type ButtonVariants = VariantProps<typeof buttonVariants>