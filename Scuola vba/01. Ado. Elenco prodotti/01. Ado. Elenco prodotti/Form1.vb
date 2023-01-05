Imports System.Data.OleDb
Public Class Form1
    Dim strconessione As String = "provider=microsoft.jet.oledb.4.0.0; data source=nw.mdb"
    Dim nmax As Integer = 100
    Dim idcategoria(nmax - 1) As Integer
    Dim n As Integer
    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim connessione As New OleDbConnection
        Dim command As New OleDbCommand
        Dim mreader As OleDbDataReader
        Dim query As String
        Try
            connessione.ConnectionString = strconessione
            connessione.Open()
            command.Connection = connessione
            query = "select nomecategoria,idcategoria from categorie"
            command.CommandText = query
            mreader = command.ExecuteReader

            Do While mreader.Read
                cmbcategoria.Items.Add(mreader("nomecategoria"))
                idcategoria(n) = mreader("idcategoria")
                n += 1
            Loop
        Catch ex As Exception
            MsgBox(ex.Message)

        End Try
    End Sub
    Private Sub cmbcategoria_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmbcategoria.SelectedIndexChanged
        Dim connessione As New OleDbConnection
        Dim command As New OleDbCommand
        Dim mreader As OleDbDataReader
        Dim query As String
        Dim r As Integer
        Try  
            connessione.ConnectionString = strconessione
            connessione.Open()
            command.Connection = connessione
            query = "select NomeProdotto,PrezzoUnitario,Scorte,LivelloDiRiordino,nomecategoria from prodotti as p inner join categorie as c on c.idcategoria = p.idcategoria where nomecategoria = '" & cmbcategoria.SelectedItem & "'"
            command.CommandText = query
            mreader = command.ExecuteReader
            dgv.Rows.Clear()
            Do While mreader.Read
                dgv.Rows.Add()
                dgv.Rows(r).Cells("NomeProdotto").Value = mreader("NomeProdotto")
                dgv.Rows(r).Cells("PrezzoUnitario").Value = mreader("PrezzoUnitario")
                dgv.Rows(r).Cells("Scorte").Value = mreader("Scorte")
                dgv.Rows(r).Cells("LivelloDiRiordino").Value = mreader("LivelloDiRiordino")
                dgv.Rows(r).Cells("categoria").Value = mreader("nomecategoria")
                r += 1
            Loop
        Catch ex As Exception
            MsgBox(ex.Message)
        End Try
    End Sub
End Class
