@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def acceptJob(request, pk):
	job = Job.objects.get(id=pk)
	booking = BookingForm(instance=job)
	educator = request.user.educator
	if request.method == "POST":
		booking.status = 'Accepted'
		booking.educator = educator
		booking.save()
		job.delete()
		return redirect('/educator')

	context = {'item':booking}

	return render(request, 'casuals/accept_job.html', context)

	@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def acceptJob(request, pk):
	job = Job.objects.get(id=pk)
	educator = request.user.educator
	booking = BookingForm(instance=job)

	if request.method == "POST":
		booking = BookingForm(request.POST, instance=job)
		if booking.is_valid():
			booking.save()
			return redirect('/educator')
		#job.delete()
#		if booking.is_valid():
#			booking.status.cleaned_data = 'Accepted'
#			booking.educator = educator
#			booking.save()
#			job.delete()
#			return redirect('/educator')

	context = {'item':job, 'educator':educator}

	return render(request, 'casuals/accept_job.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def acceptJob(request, pk):
	job = Job.objects.get(id=pk)
	educator = request.user.educator
	form = BookingForm(instance=job)

	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			job.delete()
			return redirect('/educator')
		#job.delete()
#		if booking.is_valid():
#			booking.status.cleaned_data = 'Accepted'
#			booking.educator = educator
#			booking.save()
#			job.delete()
#			return redirect('/educator')

	context = {'item':job, 'educator':educator,'form':form}

	return render(request, 'casuals/accept_job.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['educator'])
def acceptJob(request, pk):
	job = Job.objects.get(id=pk)
	educator = request.user.educator
	form = BookingForm(initial={'educator':educator, 'status':'Accepted'}, instance=job)

	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			job.delete()
			return redirect('/educator')

	context = {'item':job, 'form':form}

	return render(request, 'casuals/accept_job.html', context)