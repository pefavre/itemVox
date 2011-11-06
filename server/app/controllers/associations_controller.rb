class AssociationsController < ApplicationController
  def index
    @associations = Association.all
  end

  def show
    @association = Association.find(params[:id])
  end

  def new
    @association = Association.new
  end

  def create
    @association = Association.new(params[:association])
    if @association.save
      flash[:notice] = "Successfully created association."
      redirect_to @association
    else
      render :action => 'new'
    end
  end

  def edit
    @association = Association.find(params[:id])
  end

  def update
    @association = Association.find(params[:id])
    if @association.update_attributes(params[:association])
      flash[:notice] = "Successfully updated association."
      redirect_to association_url
    else
      render :action => 'edit'
    end
  end

  def destroy
    @association = Association.find(params[:id])
    @association.destroy
    flash[:notice] = "Successfully destroyed association."
    redirect_to associations_url
  end
end
