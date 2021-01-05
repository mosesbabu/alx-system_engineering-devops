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