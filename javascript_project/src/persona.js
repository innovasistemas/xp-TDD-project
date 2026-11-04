export class Persona {
    constructor(nombre, edad, salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    verificarMayoriaEdad() {
        return this.edad >= 18;
    }

    bonificacionSalario(bonificacion) {
        if (this.salario > 0) {
            return bonificacion * 100 / this.salario;
        }
        return 0;
    }
}