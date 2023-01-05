Imports System.Data.OleDb
Module Module1
    Public strcon As String = "provider=microsoft.jet.oledb.4.0; data source=nw.mdb"
    Sub uptadedgv(ByVal dgv As DataGridView, ByVal query As String)

        Dim connessione As New OleDbConnection
        Dim command As New OleDbCommand
        Dim mreader As OleDbDataReader
        Dim col As Integer
        Try
            connessione.ConnectionString = strcon
            connessione.Open()
            command.Connection = connessione
            command.CommandText = query
            mreader = command.ExecuteReader
            col = mreader.FieldCount - 1
            Dim r As Integer = 0
            For k = 0 To col
                dgv.Columns.Add(mreader.GetName(k), mreader.GetName(k))
            Next
            If mreader.HasRows Then
                Do While mreader.Read
                    dgv.Rows.Add()
                    For k = 0 To col
                        dgv.Rows(r).Cells(mreader.GetName(k)).Value = mreader(mreader.GetName(k))
                    Next
                    r += 1
                Loop
            End If



        Catch ex As Exception

        End Try
        



    End Sub

End Module
