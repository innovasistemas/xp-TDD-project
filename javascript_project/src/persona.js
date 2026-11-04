export class Persona {
    constructor(nombre, edad, salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    verificar_mayoria_edad() {
        return this.edad >= 18;
    }

    bonificacionSalario(bonificacion) {
        if (this.salario > 0) {
            return bonificacion * 100 / self.salario;
        }
        return 0;
    }
}