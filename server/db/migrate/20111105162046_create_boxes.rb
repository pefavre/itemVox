class CreateBoxes < ActiveRecord::Migration
  def self.up
    create_table :boxes do |t|
      t.string :lastRFID
      t.string :lastEmptyRFID

      t.timestamps
    end
  end

  def self.down
    drop_table :boxes
  end
end
