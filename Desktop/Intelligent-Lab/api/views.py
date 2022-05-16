from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerailizer
from project.models import Project, Review, Tag
from discord.models import Room
from .serializers import RoomSerailizers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET':'/api'},
        {'GET':'/api/rooms'},
        {'GET':'/api/rooms/:id'},

        {'GET':'/api/project'},
        {'GET':'/api/project/id'},
        {'POST':'/api/project/id/vote'},

        {'POST':'/api/user/token'},
        {'POST':'/api/user/token/refresh'},
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serailizer = RoomSerailizers(rooms, many=True)
    return Response(serailizer.data)


@api_view(['GET'])
def getRoom(request,pk):
    rooms = Room.objects.get(id=pk)
    serailizer = RoomSerailizers(rooms, many=False)
    return Response(serailizer.data)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializers = ProjectSerailizer(projects,many=True) #class
    return Response(serializers.data)

@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.get(id=pk)
    serializers = ProjectSerailizer(project,many=False) 
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request,pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,
    )

    review.value = data['value']
    review.save()
    project.getVoteCount

    serializers = ProjectSerailizer(project,many=False)
    return Response(serializers.data)

@api_view(['DELETE'])
def removeTag(request):
    tagid = request.data['tagId']
    projectid = request.data['projectId']

    project = Project.objects.get(id=projectid)
    tag = Tag.objects.get(id=tagid)

    project.tags.remove(tag)
    return Response('tag was deleted')