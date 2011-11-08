class CreateAssociations < ActiveRecord::Migration
  def self.up
    create_table :associations do |t|
      t.string :RFID
      t.string :URI

      t.timestamps
    end
  end

  def self.down
    drop_table :associations
  end
end
