@{
    ViewData["Title"] = "Gestión de Turnos";
}

<h2>Gestión de Turnos</h2>

<hr />

<!-- Formulario para registrar turno -->
<div>
    <h4>Registrar nuevo turno</h4>

    <form method="post" action="/Turnos/Crear">
        <div>
            <label>Número de Turno:</label><br />
            <input type="text" name="NumeroTurno" required />
        </div>

        <div>
            <label>Tipo de Atención:</label><br />
            <input type="text" name="TipoAtencion" required />
        </div>

        <br />
        <button type="submit">Registrar Turno</button>
    </form>
</div>

<hr />

<!-- Tabla de turnos -->
<div>
    <h4>Listado de Turnos</h4>

    <table border="1" cellpadding="5">
        <thead>
            <tr>
                <th>Número</th>
                <th>Fecha</th>
                <th>Tipo de Atención</th>
                <th>Estado</th>
            </tr>
        </thead>
        <tbody>
            @if (Model != null)
            {
                foreach (var turno in Model)
                {
                    <tr>
                        <td>@turno.NumeroTurno</td>
                        <td>@turno.FechaRegistro</td>
                        <td>@turno.TipoAtencion</td>
                        <td>@turno.EstadoTurno</td>
                    </tr>
                }
            }
            else
            {
                <tr>
                    <td colspan="4">No existen turnos registrados.</td>
                </tr>
            }
        </tbody>
    </table>
</div>
