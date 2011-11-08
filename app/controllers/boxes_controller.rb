class BoxesController < ApplicationController
  def index
    @boxes = Box.all
  end

  def show
    @box = Box.find(params[:id])
  end

  def new
    @box = Box.new
  end

  def create
    @box = Box.new(params[:box])
    if @box.save
      flash[:notice] = "Successfully created box."
      redirect_to @box
    else
      render :action => 'new'
    end
  end

  def edit
    @box = Box.find(params[:id])
  end

  def update
    @box = Box.find(params[:id])
    if @box.update_attributes(params[:box])
      flash[:notice] = "Successfully updated box."
      redirect_to box_url
    else
      render :action => 'edit'
    end
  end

  def destroy
    @box = Box.find(params[:id])
    @box.destroy
    flash[:notice] = "Successfully destroyed box."
    redirect_to boxes_url
  end
end
