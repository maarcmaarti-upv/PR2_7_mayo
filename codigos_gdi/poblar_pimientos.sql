--Este código puebla la BD de cada una de las tablas creadas anteriormente con el código de DDL_pimientos.sql
--Este código es de la parte perteneciente a GDI de esta entrega.

-- Proveedores

INSERT INTO pimientos.proveedor (nombre, direccion, telefono) VALUES
('AgroSur S.L.', 'Sevilla', 954123456),
('Huerta Viva', 'Almería', 950987654),
('CampoFresco', 'Murcia', 968456789);

-- Clientes

INSERT INTO pimientos.cliente (nombre, direccion, telefono) VALUES
('Mercadona', 'Valencia', 961111111),
('Carrefour', 'Madrid', 911222222),
('Lidl', 'Barcelona', 931333333);

-- Pallets

INSERT INTO pimientos.pallet (codigo, tamano, material) VALUES
('PAL001', 120.00, 'Madera'),
('PAL002', 100.00, 'Plástico'),
('PAL003', 110.00, 'Metal');

-- Cajas

INSERT INTO pimientos.caja (codigo, tamano, material, codigo_pallet) VALUES
('CAJ001', 50.00, 'Cartón', 'PAL001'),
('CAJ002', 60.00, 'Plástico', 'PAL001'),
('CAJ003', 55.00, 'Cartón', 'PAL002'),
('CAJ004', 65.00, 'Madera', 'PAL003');

-- Paquetes

INSERT INTO pimientos.paquete (codigo, tamano, material, codigo_caja) VALUES
('PAQ001', 10.00, 'Plástico', 'CAJ001'),
('PAQ002', 12.00, 'Plástico', 'CAJ001'),
('PAQ003', 11.00, 'Cartón', 'CAJ002'),
('PAQ004', 9.00, 'Cartón', 'CAJ003'),
('PAQ005', 13.00, 'Madera', 'CAJ004');

-- Lotes de Pimientos

INSERT INTO pimientos.lote_pimientos 
(numero, color, peso, procedencia, precio, codigo_paquete)
VALUES
('LOT001', 'Rojo', 100.50, 'Almería', 1.20, 'PAQ001'),
('LOT002', 'Verde', 120.00, 'Murcia', 1.10, 'PAQ002'),
('LOT003', 'Amarillo', 90.75, 'Sevilla', 1.50, 'PAQ003'),
('LOT004', 'Rojo', 110.20, 'Granada', 1.30, 'PAQ004'),
('LOT005', 'Verde', 95.00, 'Valencia', 1.15, 'PAQ005');

-- Albaranes Proveedor

INSERT INTO pimientos.albaran_proveedor (nombre, albaran) VALUES
('AgroSur S.L.', 'ALB-P-001'),
('AgroSur S.L.', 'ALB-P-002'),
('Huerta Viva', 'ALB-P-003'),
('CampoFresco', 'ALB-P-004');

-- Albaranes cliente

INSERT INTO pimientos.albaran_cliente (nombre, albaran) VALUES
('Mercadona', 'ALB-C-001'),
('Carrefour', 'ALB-C-002'),
('Lidl', 'ALB-C-003');

-- Venden (proveedor -> lote)

INSERT INTO pimientos.venden 
(proveedor, lote, transporte, km, duracion)
VALUES
('AgroSur S.L.', 'LOT001', 'Camión', 200.5, 3.5),
('AgroSur S.L.', 'LOT002', 'Camión', 180.0, 3.0),
('Huerta Viva', 'LOT003', 'Furgoneta', 150.0, 2.5),
('CampoFresco', 'LOT004', 'Camión', 220.0, 4.0),
('CampoFresco', 'LOT005', 'Tren', 300.0, 5.5);

-- COMPRADO (cliente -> pallet)

INSERT INTO pimientos.comprado
(cliente, pallet, transporte, km, duracion)
VALUES
('Mercadona', 'PAL001', 'Camión', 250.0, 4.0),
('Carrefour', 'PAL002', 'Tren', 400.0, 6.5),
('Lidl', 'PAL003', 'Camión', 350.0, 5.0);
