import { Button } from '@/components/ui/Button';
import { useToast } from '@/components/ui/use-toast';

const Pagos = () => {
  const { toast } = useToast();

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-800">Pagos</h1>
          <p className="text-gray-600 mt-2">Gestión de pagos y transacciones</p>
        </div>
        <Button 
          onClick={() => toast({ description: "🚧 This feature isn't implemented yet—but don't worry! You can request it in your next prompt! 🚀" })}
          className="bg-green-600 hover:bg-green-700"
        >
          Registrar Pago
        </Button>
      </div>

      <div className="bg-white rounded-lg shadow-md p-6">
        <p className="text-gray-600">Lista de pagos y transacciones aparecerá aquí.</p>
      </div>
    </div>
  );
};

export default Pagos;