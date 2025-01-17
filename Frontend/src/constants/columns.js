export const equipmentsColumns = [
  {
    name: "name",
    align: "left",
    label: "Nombre",
    field: "name",
    sortable: false,
  },
  {
    name: "serial_number",
    align: "left",
    label: "Nro. serie",
    field: "serial_number",
    sortable: false,
  },
  {
    name: "invoice_number",
    align: "left",
    label: "Factura",
    field: "invoice_number",
    sortable: false,
  },
  {
    name: "project_name",
    align: "left",
    label: "Proyecto",
    field: "project_name",
    sortable: true,
  },
  {
    name: "supplier_name",
    align: "left",
    label: "Proveedor",
    field: "supplier_name",
    sortable: true,
  },
  {
    name: "umag_inventory_code",
    align: "left",
    label: "Inventariado",
    field: "umag_inventory_code",
    sortable: true,
  },
  {
    name: "reception_date",
    align: "left",
    label: "Fecha",
    field: "reception_date",
    sortable: false,
  },
];

export const suppliesColumns = [
  {
    name: "name",
    align: "left",
    label: "Nombre",
    field: "name",
    sortable: false,
  },
  {
    name: "code",
    align: "left",
    label: "Código",
    field: "code",
    sortable: false,
  },
  {
    name: "supplies_brand_name",
    align: "left",
    label: "Marca",
    field: "supplies_brand_name",
    sortable: true,
  },
  {
    name: "supplies_type_name",
    align: "left",
    label: "Tipo de insumo",
    field: "supplies_type_name",
    sortable: true,
  },
  {
    name: "stock",
    align: "left",
    label: "Stock actual",
    field: "stock",
    sortable: true,
  },
  {
    name: "max_samples",
    align: "left",
    label: "Muestras",
    field: "max_samples",
    sortable: true,
  },
];

export const lotsColumns = [
  {
    name: "number",
    align: "left",
    label: "Lote",
    field: "number",
    sortable: false,
  },
  {
    name: "due_date",
    align: "left",
    label: "Fecha de vencimiento",
    field: "due_date",
    sortable: true,
  },
  {
    name: "location",
    align: "left",
    label: "Localización",
    field: "location",
    sortable: true,
  },
  {
    name: "sub_location",
    align: "left",
    label: "Sub-localización",
    field: "sub_location",
    sortable: true,
  },
  {
    name: "supplier_name",
    align: "left",
    label: "Proveedor",
    field: "supplier_name",
    sortable: false,
  },
  {
    name: "project",
    align: "left",
    label: "Proyecto",
    field: "project",
    sortable: false,
  },
  {
    name: "observations",
    align: "left",
    label: "Observación",
    field: "observations",
    sortable: false,
  },
  {
    name: "actions",
    align: "left",
    label: "Acciones",
    field: "actions",
    sortable: false,
  },
];

export const suppliersColumns = [
  {
    name: "name",
    align: "left",
    label: "Nombre",
    field: "name",
    sortable: false,
  },
  {
    name: "rut",
    align: "left",
    label: "Rut",
    field: "rut",
    sortable: false,
  },
  {
    name: "city_address",
    align: "left",
    label: "Dirección",
    field: "city_address",
    sortable: false,
  }
]

export const suppliersSupplyColumns = [
  {
    name: "name",
    align: "left",
    label: "Nombre",
    field: "name",
    sortable: false,
  },
  {
    name: "rut",
    align: "left",
    label: "Rut",
    field: "rut",
    sortable: false,
  },
  {
    name: "city_address",
    align: "left",
    label: "Dirección",
    field: "city_address",
    sortable: false,
  },
  {
    name: "cost",
    align: "left",
    label: "Costo",
    field: "cost",
    sortable: false,
  }
]

export const rolOptions = [
  {
    value: "Vendedor",
    name: "Vendedor",
  },
  {
    value: "Tecnico",
    name: "Técnico",
  },
];

export const columns_maintenances = [
  {
    name: "maintenance_type",
    align: "left",
    label: "Tipo mantenimiento",
    field: "maintenance_type",
    sortable: true,
  },
  {
    name: "state",
    align: "left",
    label: "Realizado",
    field: "state",
    sortable: true,
  },
  {
    name: "date",
    align: "left",
    label: "Fecha",
    field: "date",
    sortable: true,
  },
  {
    name: "observations",
    align: "left",
    label: "Observaciones",
    field: "observations",
    sortable: false,
  },
  {
    name: "actions",
    align: "left",
    label: "Acciones",
    field: "actions",
    sortable: false,
  },
];