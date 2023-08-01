"""init

Revision ID: e6f26b3809aa
Revises: 
Create Date: 2023-08-01 18:11:58.667503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6f26b3809aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Brands',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Buildings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Locations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Project_owners',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Suppliers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('rut', sa.String(), nullable=False),
    sa.Column('city_address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Supplies_brands',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Supplies_formats',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Supplies_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('disable', sa.Boolean(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('Invoices',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['supplier_id'], ['Suppliers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Models',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['Brands.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Projects',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['Project_owners.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Sub_locations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['Locations.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Supplier_contact',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('position', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['Suppliers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Supplies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('lot_stock', sa.Integer(), nullable=False),
    sa.Column('critical_stock', sa.Integer(), nullable=False),
    sa.Column('samples', sa.Float(), nullable=False),
    sa.Column('observation', sa.String(), nullable=False),
    sa.Column('supplies_brand_id', sa.Integer(), nullable=False),
    sa.Column('supplies_type_id', sa.Integer(), nullable=False),
    sa.Column('supplies_format_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['supplies_brand_id'], ['Supplies_brands.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['supplies_format_id'], ['Supplies_formats.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['supplies_type_id'], ['Supplies_types.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Units',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('building_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['building_id'], ['Buildings.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Lots',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('observations', sa.String(), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=False),
    sa.Column('supplies_id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('sub_location_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['Projects.id'], ),
    sa.ForeignKeyConstraint(['sub_location_id'], ['Sub_locations.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['Suppliers.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['supplies_id'], ['Supplies.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Model_numbers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['model_id'], ['Models.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Rooms',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('unit_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['unit_id'], ['Units.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Stages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['Projects.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Suppliers_has_Supplies',
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('supply_id', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['Suppliers.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['supply_id'], ['Supplies.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('supplier_id', 'supply_id')
    )
    op.create_table('Equipments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('serial_number', sa.String(), nullable=True),
    sa.Column('umag_inventory_code', sa.String(), nullable=True),
    sa.Column('reception_date', sa.Date(), nullable=True),
    sa.Column('maintenance_period', sa.Integer(), nullable=True),
    sa.Column('observation', sa.String(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('invoice_id', sa.Integer(), nullable=True),
    sa.Column('model_number_id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('stage_id', sa.Integer(), nullable=True),
    sa.Column('last_preventive_mainteinance', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['invoice_id'], ['Invoices.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['model_number_id'], ['Model_numbers.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['room_id'], ['Rooms.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['stage_id'], ['Stages.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['supplier_id'], ['Suppliers.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Maintenances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('observations', sa.String(), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=True),
    sa.Column('equiptment_id', sa.Integer(), nullable=False),
    sa.Column('maintenance_type', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['equiptment_id'], ['Equipments.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Maintenances')
    op.drop_table('Equipments')
    op.drop_table('Suppliers_has_Supplies')
    op.drop_table('Stages')
    op.drop_table('Rooms')
    op.drop_table('Model_numbers')
    op.drop_table('Lots')
    op.drop_table('Units')
    op.drop_table('Supplies')
    op.drop_table('Supplier_contact')
    op.drop_table('Sub_locations')
    op.drop_table('Projects')
    op.drop_table('Models')
    op.drop_table('Invoices')
    op.drop_table('Users')
    op.drop_table('Supplies_types')
    op.drop_table('Supplies_formats')
    op.drop_table('Supplies_brands')
    op.drop_table('Suppliers')
    op.drop_table('Project_owners')
    op.drop_table('Locations')
    op.drop_table('Buildings')
    op.drop_table('Brands')
    # ### end Alembic commands ###
