import test from 'node:test';
import assert from 'node:assert';
import { Persona } from '../src/persona.js' // Importación directa

test('Una persona de 25 años debe ser mayor de edad', () => {
    // Preparar (Arrange)
    const persona = new Persona("Ana", 25, 2000000);

    // Actuar (Act)
    const resultado = persona.verificar_mayoria_edad();

    // Afirmar (Assert)
    assert.strictEqual(resultado, true);
});

test('Una persona de 10 años no es mayor de edad', () => {
    const persona = new Persona("Hugo", 10, 0);
    assert.strictEqual(persona.verificar_mayoria_edad(), false)
});